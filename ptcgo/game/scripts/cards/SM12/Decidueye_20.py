from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from ptcgo.game.card_effects.attacks_common import snipe_attack
from ptcgo.game.card_effects.passives_common import is_in_active_spot


def _benched_damaged(pokemon):
    if is_in_active_spot(pokemon):
        return False
    maximum = pokemon.attribute_originals.get(
        AttrID.HP.value, pokemon.get_attribute(AttrID.HP, 0))
    return pokemon.get_attribute(AttrID.HP, 0) < maximum

card = PokemonCardDef(
    guid="e757cef4-abc6-5a3d-9e62-3e021f67e56a",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Decidueye.Name",
    display_name="Decidueye",
    searchable_by=["Decidueye", "Stage 2", "Decidueye"],
    subtypes=["Stage 2"],
    collector_number=20,
    set_code="SM12",
    rarity=Rarities.RareHolo,
    hp=140,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Dartrix.Name",
    family_id=722,
    abilities=[
        Attack(
            title="Skill Dive",
            game_text="This attack does 40 damage to 1 of your opponent's Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.GRASS: 1},
            effect=snipe_attack(40, pool="any", count=1),
        ),
        Attack(
            title="Tracking Shot",
            game_text="This attack does 80 damage to 1 of your opponent's Benched Pok\u00e9mon that has any damage counters on it. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.COLORLESS: 2},
            damage=80,
            effect=snipe_attack(80, pool=_benched_damaged, count=1),
        ),
    ],
)