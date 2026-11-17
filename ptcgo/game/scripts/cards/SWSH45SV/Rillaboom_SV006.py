from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="e1213b61-569c-59f8-930e-7057f73f700a",
    key="SWSH45SV",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Rillaboom.Name",
    display_name="Rillaboom",
    searchable_by=["Rillaboom", "Stage 2", "Rillaboom"],
    subtypes=["Stage 2"],
    collector_number=6,
    set_code="SWSH45SV",
    rarity=Rarities.Rare,
    hp=170,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Thwackey.Name",
    family_id=810,
    abilities=[
        Ability(
            title="Voltage Beat",
            game_text="Once during your turn, you may search your deck for up to 2 Grass Energy cards and attach them to 1 of your Pok\u00e9mon. Then, shuffle your deck.",
            effect=unimplemented,
        ),
        Attack(
            title="Hammer In",
            cost={PokemonTypes.GRASS: 3, PokemonTypes.COLORLESS: 1},
            damage=140,
        ),
    ],
)