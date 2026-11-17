from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="d2282c95-0ec1-53fa-880c-703c52238a89",
    key="PL1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DialgaG.Name",
    display_name="Dialga G",
    searchable_by=["Dialga G", "Basic", "SP", "DialgaG"],
    subtypes=["Basic", "SP"],
    collector_number=7,
    set_code="PL1",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=483,
    abilities=[
        Attack(
            title="Deafen",
            game_text="Your opponent can't play any Trainer cards or Stadium cards from his or her hand during your opponent's next turn.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=unimplemented,
        ),
        Attack(
            title="Second Strike",
            game_text="If the Defending Pok\u00e9mon already has 2 or more damage counters on it, this attack does 50 damage plus 20 more damage.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)