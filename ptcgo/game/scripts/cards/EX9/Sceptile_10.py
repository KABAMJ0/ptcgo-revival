from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.passives_common import condition_immunity_passive
from ptcgo.game.card_effects.pokemon import energy_provides_type
from ptcgo.game.session.passives import carrier_pokemon
from ptcgo.game.card_effects.attacks_common import ignore_modifier_attack

def _green_essence_target(target, carrier):
    holder = carrier_pokemon(carrier)
    if holder is None or target.owning_player_id != holder.owning_player_id:
        return False
    from ptcgo.game.card_effects.passives_common import is_in_active_spot
    if not is_in_active_spot(target):
        return False
    return any(energy_provides_type(child, PokemonTypes.GRASS.value)
               for child in target.children)

card = PokemonCardDef(
    guid="53891197-337b-545a-8e84-b6b8c1ece227",
    key="EX9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sceptile.Name",
    display_name="Sceptile",
    searchable_by=["Sceptile", "Stage 2", "Sceptile"],
    subtypes=["Stage 2"],
    collector_number=10,
    set_code="EX9",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Grovyle.Name",
    family_id=252,
    abilities=[
        Ability(
            title="Green Essence",
            game_text="As long as Sceptile is in play, each of your Active Pok\u00e9mon that has Grass Energy attached to it can't be affected by any Special Conditions.",
            effect=None,
            passive=condition_immunity_passive(None, protects=_green_essence_target),
        ),
        Attack(
            title="Razor Leaf",
            cost={PokemonTypes.GRASS: 1},
            damage=30,
        ),
        Attack(
            title="Swift",
            game_text="This attack's damage isn't affected by Weakness, Resistance, Pok\u00e9-Powers, Pok\u00e9-Bodies, or any other effects on the Defending Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 3},
            damage=60,
            effect=ignore_modifier_attack(ignore_weakness=True, ignore_resistance=True, ignore_target_effects=True),
        ),
    ],
)