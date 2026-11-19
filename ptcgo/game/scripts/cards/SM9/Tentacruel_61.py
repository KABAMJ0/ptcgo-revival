from ptcgo.game.card_effects.attacks_common import condition_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, subtypes_for
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from ptcgo.game.card_effects.passives_common import protect_next_turn


def _attacker_has_subtype(*names):
    def pred(attacker):
        return attacker is not None and any(
            name in (subtypes_for(attacker.archetype_id) or [])
            for name in names)
    return pred
from ptcgo.game.attributes import SpecialConditions
from ptcgo.game.card_effects.attacks_common import condition_attack


card = PokemonCardDef(
    guid="dc6dd5a2-1d2f-5cac-baeb-af0448f9f71a",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tentacruel.Name",
    display_name="Tentacruel",
    searchable_by=["Tentacruel", "Stage 1", "Tentacruel"],
    subtypes=["Stage 1"],
    collector_number=61,
    set_code="SM9",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Tentacool.Name",
    family_id=72,
    abilities=[
        Attack(
            title="Void Tentacles",
            game_text="Your opponent's Active Pok\u00e9mon is now Confused and Poisoned.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=condition_attack(SpecialConditions.CONFUSED, SpecialConditions.POISONED),
        ),
        Attack(
            title="Paranormal",
            game_text="During your opponent's next turn, prevent all damage done to this Pok\u00e9mon by attacks from Ultra Beasts.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
            effect=protect_next_turn(prevent=True, attacker_pred=_attacker_has_subtype("Ultra Beast")),
        ),
    ],
)