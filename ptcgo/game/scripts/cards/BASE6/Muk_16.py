from ptcgo.game.card_effects.attacks_common import condition_attack
from ptcgo.game.card_effects.passives_common import ability_lock_passive
from ptcgo.game.attributes import AttrID
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, def_for
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions

def _ignores_powers(pokemon, carrier):
    """Every Pokemon Power other than Toxic Gases: a Toxic Gas is never
    switched off by another one, and this power stops while Muk itself is
    affected by a Special Condition."""
    if carrier.get_attribute(AttrID.SPECIAL_CONDITIONS) or []:
        return False
    definition = def_for(pokemon.archetype_id)
    return not any(getattr(ability, "title", "") == "Toxic Gas"
                   for ability in (getattr(definition, "abilities", None) or []))


card = PokemonCardDef(
    guid="f7fdae30-cb57-57e5-bc87-f69c75ab6f40",
    key="BASE6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Muk.Name",
    display_name="Muk",
    searchable_by=["Muk", "Stage 1", "Muk"],
    subtypes=["Stage 1"],
    collector_number=16,
    set_code="BASE6",
    rarity=Rarities.RareHolo,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Grimer.Name",
    family_id=88,
    abilities=[
        Ability(
            title="Toxic Gas",
            game_text="Ignore all Pok\u00e9mon Powers other than Toxic Gases. This power stops working while Muk is affected by a Special Condition.",
            passive=ability_lock_passive(_ignores_powers),
        ),
        Attack(
            title="Sludge",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Poisoned.",
            cost={PokemonTypes.GRASS: 3},
            damage=30,
            effect=condition_attack(SpecialConditions.POISONED, flip=True),
        ),
    ],
)