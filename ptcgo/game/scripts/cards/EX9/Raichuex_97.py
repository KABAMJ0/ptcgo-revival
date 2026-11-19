from ptcgo.game.card_effects.attacks_common import snipe_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.pokemon import is_pokemon_ex
from ptcgo.game.card_effects.passives_common import takes_less_passive
from ptcgo.game.content.definitions import def_for

def _rai_shield_target(target, carrier):
    if target.owning_player_id != carrier.owning_player_id:
        return False
    definition = def_for(target.archetype_id)
    return definition is not None and definition.display_name == "Raichu ex"


def _opponent_ex(attacker):
    return attacker is not None and is_pokemon_ex(attacker)

card = PokemonCardDef(
    guid="6b7f75c1-fd15-5bb7-a6ca-66ac7f24a7d3",
    key="EX9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Raichuex.Name",
    display_name="Raichu ex",
    searchable_by=["Raichu ex", "Stage 1", "ex", "Raichuex"],
    subtypes=["Stage 1", "ex"],
    collector_number=97,
    set_code="EX9",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Pikachu.Name",
    family_id=25,
    abilities=[
        Ability(
            title="Rai-shield",
            game_text="Damage done to any of your Raichu ex in play by attacks from your opponent's Pok\u00e9mon-ex is reduced by 30 (after applying Weakness and Resistance). You can't use more than 1 Rai-shield Pok\u00e9-Body each turn.",
            effect=None,
            passive=takes_less_passive(30, protects=_rai_shield_target, attacker_pred=_opponent_ex, stack_key="Rai-shield"),
        ),
        Attack(
            title="Power Short",
            game_text="Choose 1 of your opponent's Pok\u00e9mon. This attack does 30 damage to that Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.) If that Pok\u00e9mon has Pok\u00e9-Powers, this attack does 30 damage plus 20 more damage.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            effect=snipe_attack(30, pool="any"),
        ),
        Attack(
            title="Pika Bolt",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 3},
            damage=70,
        ),
    ],
)