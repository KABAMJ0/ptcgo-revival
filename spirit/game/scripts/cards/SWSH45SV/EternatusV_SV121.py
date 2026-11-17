from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="85c28d24-135d-512c-b332-d73f87b3b531",
    key="SWSH45SV",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.EternatusV.Name",
    display_name="Eternatus V",
    searchable_by=["Eternatus V", "Basic", "V", "EternatusV"],
    subtypes=["Basic", "V"],
    collector_number=121,
    set_code="SWSH45SV",
    rarity=Rarities.RareSecret,
    hp=220,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=890,
    abilities=[
        Attack(
            title="Power Accelerator",
            game_text="You may attach a Darkness Energy card from your hand to 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=unimplemented,
        ),
        Attack(
            title="Dynamax Cannon",
            game_text="If your opponent's Active Pok\u00e9mon is a Pok\u00e9mon VMAX, this attack does 120 more damage.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 3},
            damage=120,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)