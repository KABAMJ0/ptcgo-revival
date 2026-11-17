from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="c9f34e4f-7854-5b94-a2bc-a18d48795b13",
    key="SWSH11TG",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.EternatusVMAX.Name",
    display_name="Eternatus VMAX",
    searchable_by=["Eternatus VMAX", "VMAX", "Eternamax", "EternatusVMAX"],
    subtypes=["VMAX", "Eternamax"],
    collector_number=22,
    set_code="SWSH11TG",
    rarity=Rarities.RareHoloVMAX,
    hp=340,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.VMAX,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.EternatusV.Name",
    family_id=890,
    abilities=[
        Ability(
            title="Eternal Zone",
            game_text="If all of your Pok\u00e9mon in play are Darkness type, you can have up to 8 Pok\u00e9mon on your Bench, and you can't put non-Darkness Pok\u00e9mon into play. (If this Ability stops working, discard Pok\u00e9mon from your Bench until you have 5.)",
            effect=unimplemented,
        ),
        Attack(
            title="Dread End",
            game_text="This attack does 30 damage for each of your Darkness Pok\u00e9mon in play.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)