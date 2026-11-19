from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import gust_attack

card = PokemonCardDef(
    guid="7ed4bf00-732f-5571-b23e-56527b6675fc",
    key="EX4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamMagmasPoochyena.Name",
    display_name="Team Magma's Poochyena",
    searchable_by=["Team Magma's Poochyena", "Basic", "TeamMagmasPoochyena"],
    subtypes=["Basic"],
    collector_number=66,
    set_code="EX4",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=261,
    abilities=[
        Attack(
            title="Darkness Call",
            game_text="Your opponent switches the Defending Pok\u00e9mon with 1 of his or her Benched Pok\u00e9mon, if any.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=gust_attack(opponent_chooses=True),
        ),
        Attack(
            title="Sharp Fang",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)