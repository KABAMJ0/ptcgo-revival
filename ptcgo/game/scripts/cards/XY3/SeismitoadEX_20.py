from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="05b1a304-d59a-5cc8-94fa-6bf11e28274e",
    key="XY3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.SeismitoadEX.Name",
    display_name="Seismitoad-EX",
    searchable_by=["Seismitoad-EX", "Basic", "EX", "SeismitoadEX"],
    subtypes=["Basic", "EX"],
    collector_number=20,
    set_code="XY3",
    rarity=Rarities.RareHolo,
    hp=180,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    family_id=537,
    abilities=[
        Attack(
            title="Quaking Punch",
            game_text="Your opponent can't play any Item cards from his or her hand during his or her next turn.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=unimplemented,
        ),
        Attack(
            title="Grenade Hammer",
            game_text="This attack does 30 damage to 2 of your Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=130,
            effect=unimplemented,
        ),
    ],
)