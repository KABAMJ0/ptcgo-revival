from ptcgo.game.card_effects.attacks_common import condition_attack
from ptcgo.game.card_effects.passives_common import attack_effect_shield_passive
from ptcgo.game.card_effects.support_common import entity_name
from ptcgo.game.session.passives import carrier_pokemon


def _has_react_energy(target, carrier) -> bool:
    """Only Mew itself, and only while a React Energy card rides it."""
    holder = carrier_pokemon(carrier)
    if target is None or holder is None or holder is not target:
        return False
    return any("react energy" in entity_name(energy).lower()
               for energy in target.children)
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from ptcgo.game.card_effects.attacks_common import condition_attack

card = PokemonCardDef(
    guid="88ebcffa-dc4f-53fd-b9c2-4b30126e88b1",
    key="POP4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mew.Name",
    display_name="Mew",
    searchable_by=["Mew", "Basic", "Mew"],
    subtypes=["Basic"],
    collector_number=4,
    set_code="POP4",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=151,
    abilities=[
        Ability(
            title="Reactive Barrier",
            game_text="As long as Mew has any React Energy cards attached to it, prevent all effects, excluding damage, done to Mew by attacks from your opponent's Pok\u00e9mon.",
            passive=attack_effect_shield_passive(protects=_has_react_energy),
        ),
        Attack(
            title="Psyshock",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
    ],
)