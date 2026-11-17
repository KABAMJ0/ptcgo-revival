from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="0e638304-8854-5253-9462-a6ff697c0a6e",
    key="SV9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Furret.Name",
    display_name="Furret",
    searchable_by=["Furret", "Stage 1", "Furret"],
    subtypes=["Stage 1"],
    collector_number=168,
    set_code="SV9",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Sentret.Name",
    family_id=161,
    abilities=[
        Attack(
            title="Scratch",
            cost={PokemonTypes.COLORLESS: 1},
            damage=40,
        ),
        Attack(
            title="Jet Headbutt",
            cost={PokemonTypes.COLORLESS: 2},
            damage=70,
        ),
    ],
)