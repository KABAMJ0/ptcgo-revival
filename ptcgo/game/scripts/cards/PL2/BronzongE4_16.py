from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="6d4fd557-83de-512f-aceb-b962be296ec2",
    key="PL2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.BronzongE4.Name",
    display_name="Bronzong E4",
    searchable_by=["Bronzong E4", "Basic", "SP", "BronzongE4"],
    subtypes=["Basic", "SP"],
    collector_number=16,
    set_code="PL2",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    resistance_type=PokemonTypes.FIRE,
    family_id=437,
    abilities=[
        Attack(
            title="Hand Refresh",
            game_text="Each player shuffles his or her hand into his or her deck and draws up to 4 cards. (You draw your cards first.)",
            cost={},
            effect=unimplemented,
        ),
        Attack(
            title="Payback",
            game_text="If your opponent has only 1 Prize card left, this attack does 10 damage plus 50 more damage and the Defending Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)