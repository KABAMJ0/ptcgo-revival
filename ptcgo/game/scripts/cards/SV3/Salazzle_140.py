from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="ed0d1508-61d9-5675-8410-4d2e488e21d8",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Salazzle.Name",
    display_name="Salazzle",
    searchable_by=["Salazzle", "Stage 1", "Salazzle"],
    subtypes=["Stage 1"],
    collector_number=140,
    set_code="SV3",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Salandit.Name",
    family_id=757,
    abilities=[
        Attack(
            title="Suffocating Gas",
            cost={PokemonTypes.DARKNESS: 1},
            damage=40,
        ),
        Attack(
            title="Gentle Slap",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=70,
        ),
    ],
)