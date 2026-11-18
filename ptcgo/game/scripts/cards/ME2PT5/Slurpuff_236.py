from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="39c73381-7c24-5473-a0ca-20a709c804c8",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Slurpuff.Name",
    display_name="Slurpuff",
    searchable_by=["Slurpuff", "Stage 1", "Slurpuff"],
    subtypes=["Stage 1"],
    collector_number=236,
    set_code="ME2PT5",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Swirlix.Name",
    family_id=684,
    abilities=[
        Attack(
            title="Tackle",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=40,
        ),
        Attack(
            title="Magical Shot",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=70,
        ),
    ],
)