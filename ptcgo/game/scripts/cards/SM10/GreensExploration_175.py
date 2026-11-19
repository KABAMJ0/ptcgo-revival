from ptcgo.game.data_utils import SupporterCardDef, def_for
from ptcgo.game.attributes import AbilityTypes, Rarities
from ptcgo.game.card_effects.support_common import search_to_hand
from ptcgo.game.card_effects.trainers import is_trainer_card

_ATTACK_TYPES = (AbilityTypes.ATTACK, AbilityTypes.NON_DAMAGING_ATTACK)


def _no_pokemon_with_abilities():
    """Play condition: none of your Pokemon in play prints a PokeAbility. An
    attack is not an Ability; the entity's PIE_ABILITIES carries both, so this
    reads the definition and skips the attack rows."""
    def check(board, player_id):
        for pokemon in board.pokemon_in_play(player_id):
            definition = def_for(pokemon.archetype_id)
            for ability in getattr(definition, "abilities", None) or []:
                if getattr(ability, "ability_type", None) not in _ATTACK_TYPES:
                    return False
        return True
    return check

card = SupporterCardDef(
    guid="227a00bb-895e-553a-91d4-f11b64bfc756",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.GreensExploration.Name",
    display_name="Green's Exploration",
    searchable_by=["Green's Exploration", "Supporter"],
    subtypes=["Supporter"],
    collector_number=175,
    set_code="SM10",
    rarity=Rarities.Uncommon,
    effect=search_to_hand(is_trainer_card, count=2), condition=_no_pokemon_with_abilities()
)
