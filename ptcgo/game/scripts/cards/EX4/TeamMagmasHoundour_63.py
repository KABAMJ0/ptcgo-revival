from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import gust_attack

card = PokemonCardDef(
    guid="7dd6eadc-9738-529c-b7d5-0cecd35cd7b8",
    key="EX4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamMagmasHoundour.Name",
    display_name="Team Magma's Houndour",
    searchable_by=["Team Magma's Houndour", "Basic", "TeamMagmasHoundour"],
    subtypes=["Basic"],
    collector_number=63,
    set_code="EX4",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=228,
    abilities=[
        Attack(
            title="Kick Away",
            game_text="Your opponent switches the Defending Pok\u00e9mon with 1 of his or her Benched Pok\u00e9mon, if any.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=gust_attack(opponent_chooses=True),
        ),
        Attack(
            title="Steady Firebreathing",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)