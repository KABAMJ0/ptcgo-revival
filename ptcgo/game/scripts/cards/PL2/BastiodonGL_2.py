from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="895b1258-6465-504e-b584-257f37fc0ef6",
    key="PL2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.BastiodonGL.Name",
    display_name="Bastiodon GL",
    searchable_by=["Bastiodon GL", "Basic", "SP", "BastiodonGL"],
    subtypes=["Basic", "SP"],
    collector_number=2,
    set_code="PL2",
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=411,
    abilities=[
        Attack(
            title="Bounce Back",
            game_text="Your opponent switches the Defending Pok\u00e9mon with 1 of his or her Benched Pok\u00e9mon.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=unimplemented,
        ),
        Attack(
            title="Smack Attack",
            game_text="Remove 1 damage counter from Bastiodon GL.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 3},
            damage=60,
            effect=unimplemented,
        ),
    ],
)