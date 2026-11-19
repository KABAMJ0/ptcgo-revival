from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, Triggers, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import search_to_hand
from ptcgo.game.session.effects import is_supporter_card
from ptcgo.game.card_effects.attacks_common import condition_attack
from ptcgo.game.attributes import SpecialConditions


card = PokemonCardDef(
    guid="8069e1c4-479b-5a90-83b5-fd82c4ccfbbe",
    key="BW10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.JirachiEX.Name",
    display_name="Jirachi-EX",
    searchable_by=["Jirachi-EX", "Basic", "EX", "JirachiEX"],
    subtypes=["Basic", "EX"],
    collector_number=98,
    set_code="BW10",
    rarity=Rarities.RareUltra,
    hp=90,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=385,
    abilities=[
        Ability(
            title="Stellar Guidance",
            game_text="When you play this Pok\u00e9mon from your hand onto your Bench, you may search your deck for a Supporter card, reveal it, and put it into your hand. Shuffle your deck afterward.",
            trigger=Triggers.ON_PLAY,
            effect=search_to_hand(is_supporter_card, count=1, reveal=True),
        ),
        Attack(
            title="Hypnostrike",
            game_text="Both this Pok\u00e9mon and the Defending Pok\u00e9mon are now Asleep.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=condition_attack(SpecialConditions.ASLEEP, both_actives=True),
        ),
    ],
)