from ptcgo.game.card_effects.attacks_common import flip_bonus
from ptcgo.game.card_effects.passives_common import Passive
from ptcgo.game.card_effects.pokemon import energy_provides_type
from ptcgo.game.session.passives import carrier_pokemon
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import flip_bonus

class _WeakBarrierPassive(Passive):
    """No Weakness while a Psychic Energy is attached to this Pokemon."""

    def modify_weakness(self, calc, carrier):
        holder = carrier_pokemon(carrier)
        if holder is None or calc.target is not holder:
            return
        if any(energy_provides_type(e, PokemonTypes.PSYCHIC.value)
               for e in (holder.children or [])):
            calc.weakness_applies = False


card = PokemonCardDef(
    guid="19992996-48af-5421-8fdf-7e4fb2b9b09e",
    key="Promo_BW",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Elgyem.Name",
    display_name="Elgyem",
    searchable_by=["Elgyem", "Basic", "Elgyem"],
    subtypes=["Basic"],
    collector_number=55,
    set_code="Promo_BW",
    rarity=Rarities.RarePromo,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=605,
    abilities=[
        Ability(
            title="Weak Barrier",
            game_text="If this Pok\u00e9mon has any Psychic Energy attached to it, this Pok\u00e9mon has no Weakness.",
            passive=_WeakBarrierPassive(),
        ),
        Attack(
            title="Quick Blow",
            game_text="Flip a coin. If heads, this attack does 20 more damage.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=10,
            damage_operator="+",
            effect=flip_bonus(20),
        ),
    ],
)