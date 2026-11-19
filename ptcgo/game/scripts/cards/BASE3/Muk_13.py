from ptcgo.game.card_effects.attacks_common import condition_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from ptcgo.game.attributes import AttrID
from ptcgo.game.data_utils import def_for
from ptcgo.game.session.passives import Passive, carrier_pokemon


def _has_toxic_gas(pokemon) -> bool:
    definition = def_for(getattr(pokemon, "archetype_id", "") or "")
    return any(getattr(ability, "title", "") == "Toxic Gas"
               for ability in (getattr(definition, "abilities", []) or []))


class _ToxicGas(Passive):
    """Every Pokemon Power other than a Toxic Gas is ignored, on both sides;
    off while the holder is Asleep, Confused or Paralyzed. The exception is
    read off each Pokemon's own printed abilities, so a second Muk copy does
    not lock this one out."""

    def blocks_abilities(self, pokemon, carrier):
        holder = carrier_pokemon(carrier)
        if holder.get_attribute(AttrID.SPECIAL_CONDITIONS):
            return False
        return not _has_toxic_gas(pokemon)


_toxic_gas = _ToxicGas()

card = PokemonCardDef(
    guid="c2f578f8-7fb1-503c-a09e-32d6b8b4388a",
    key="BASE3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Muk.Name",
    display_name="Muk",
    searchable_by=["Muk", "Stage 1", "Muk"],
    subtypes=["Stage 1"],
    collector_number=13,
    set_code="BASE3",
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
            game_text="Ignore all Pok\u00e9mon Powers other than Toxic Gases. This power stops working while Muk is Asleep, Confused, or Paralyzed.",
            passive=_toxic_gas,
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