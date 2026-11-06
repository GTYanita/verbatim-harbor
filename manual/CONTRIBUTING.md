# 开发证据流水线

`evidence_pipeline/adaptive_evidence/` 包含服务与证据处理模块；回归检查位于 `checks/`，部署文件位于 `operations/`。以下命令均从仓库根目录执行。

## 本地检查

在独立虚拟环境中安装开发包并运行已有测试：

```shell
python -m pip install -e .
python -m unittest discover -s checks -p "test_*.py"
```

这些检查使用合成记录与模拟编码器。运行实际服务还需安装根目录 `requirements.txt`，并在仓库外配置服务凭据及数据目录。

## 容器与运行材料

```shell
docker build -f operations/Dockerfile .
```

Compose 文件为 `operations/compose.yaml`。部署步骤见 [DEPLOYMENT.md](DEPLOYMENT.md)，接口和提交记录见 [SUBMISSION.md](SUBMISSION.md)。开发安装不会自动部署服务。

## 文件核验

```shell
python tools/verify_layout.py
python tools/verify_layout.py --frozen-only
```

第一条检查当前开发文件，第二条检查保留的固定发布文件。历史发布身份仍以相应提交及原清单为准。依赖、方法与来源记录见根目录 [PROVENANCE.md](../PROVENANCE.md)，许可见 [LICENSE](../LICENSE)。
