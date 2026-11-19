from ptcgo.game.card_effects.attacks_common import damage_per, recoil_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import AttrID, PokemonTypes, PokemonStage, Rarities
from ptcgo.game.data_utils import def_for
from ptcgo.game.session.passives import effective_max_hp
from ptcgo.game.card_effects.attacks_common import recoil_attack


def _damaged_tauros(ctx) -> int:
    """Your Pokemon named Tauros that carry any damage counters."""
    count = 0
    for pokemon in ctx.my_pokemon_in_play():
        definition = def_for(pokemon.archetype_id)
        if "tauros" not in (getattr(definition, "display_name", "") or "").lower():
            continue
        if pokemon.get_attribute(AttrID.HP, 0) < effective_max_hp(ctx.board, pokemon):
            count += 1
    return count


card = PokemonCardDef(
    guid="ad30ccbc-8d0c-5dbd-bc66-71031b319d70",
    key="ME2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.PaldeanTauros.Name",
    display_name="Paldean Tauros",
    searchable_by=["Paldean Tauros", "Basic", "PaldeanTauros"],
    subtypes=["Basic"],
    collector_number=48,
    set_code="ME2",
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=128,
    abilities=[
        Attack(
            title="Raging Charge",
            game_text="This attack does 40 damage for each of your Pok\u00e9mon that has \"Tauros\" in its name that has any damage counters on it.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=40,
            damage_operator="x",
            effect=damage_per(_damaged_tauros, 40),
        ),
        Attack(
            title="Double-Edge",
            game_text="This Pok\u00e9mon also does 20 damage to itself.",
            cost={PokemonTypes.FIGHTING: 2},
            damage=70,
            effect=recoil_attack(20),
        ),
    ],
)