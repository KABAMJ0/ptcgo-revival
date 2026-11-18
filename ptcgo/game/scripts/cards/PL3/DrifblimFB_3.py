from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="e9628e32-8d7e-5ae5-b981-82cac57e2cbb",
    key="PL3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DrifblimFB.Name",
    display_name="Drifblim FB",
    searchable_by=["Drifblim FB", "Basic", "SP", "DrifblimFB"],
    subtypes=["Basic", "SP"],
    collector_number=3,
    set_code="PL3",
    rarity=Rarities.RareHolo,
    hp=80,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.COLORLESS,
    family_id=426,
    abilities=[
        Ability(
            title="Pump Up",
            game_text="If your opponent has 3 or less Prize cards left, Drifblim FB gets +40 HP.",
            effect=unimplemented,
        ),
        Attack(
            title="Shadow Ball",
            game_text="Choose 1 of your opponent's Benched Pok\u00e9mon. This attack does 40 damage to that Pok\u00e9mon. Apply Weakness and Resistance.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            effect=unimplemented,
        ),
    ],
)