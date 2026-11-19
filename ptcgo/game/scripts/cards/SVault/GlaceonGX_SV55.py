from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import snipe_attack
from ptcgo.game.card_effects.attacks_common import damage_per, damage_counters_on


from ptcgo.game.card_effects.passives_common import ability_lock_passive
from ptcgo.game.data_utils import has_rule_box


def _their_rule_box(pokemon, carrier):
    if pokemon.owning_player_id == carrier.owning_player_id:
        return False
    return has_rule_box(pokemon.archetype_id)


_freezing_gaze = ability_lock_passive(_their_rule_box)

card = PokemonCardDef(
    guid="e9cc02c1-f5a4-5f17-be7c-46dbdcd864ec",
    key="SVault",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GlaceonGX.Name",
    display_name="Glaceon-GX",
    searchable_by=["Glaceon-GX", "Stage 1", "GX", "GlaceonGX"],
    subtypes=["Stage 1", "GX"],
    collector_number=55,
    set_code="SVault",
    rarity=Rarities.Rare,
    hp=200,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    family_id=133,
    abilities=[
        Ability(
            title="Freezing Gaze",
            game_text="As long as this Pok\u00e9mon is your Active Pok\u00e9mon, your opponent's Pok\u00e9mon-GX and Pok\u00e9mon-EX in play, in their hand, and in their discard pile have no Abilities, except for Freezing Gaze.",
            passive=_freezing_gaze,
        ),
        Attack(
            title="Frost Bullet",
            game_text="This attack does 30 damage to 1 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=90,
            effect=snipe_attack(30, pool="bench", count=1, apply_modifiers=False),
        ),
        Attack(
            title="Polar Spear-GX",
            game_text="This attack does 50 damage for each damage counter on your opponent's Active Pok\u00e9mon. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            damage_operator="x",
            effect=damage_per(damage_counters_on('defender'), 50),
        ),
    ],
)