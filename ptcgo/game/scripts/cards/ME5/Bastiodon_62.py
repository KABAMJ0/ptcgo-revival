from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.passives_common import is_in_active_spot
from ptcgo.game.card_effects.pokemon import is_energy_card
from ptcgo.game.session.passives import Passive, carrier_pokemon


def _attacker_energy_count(attacker) -> int:
    return sum(1 for child in attacker.children if is_energy_card(child))


class AncientBulwarkPassive(Passive):
    """While this Pokemon is on your Bench, none of your Pokemon takes damage
    from an opponent's attacker that holds 2 or less Energy."""

    def prevents_damage(self, calc, carrier):
        holder = carrier_pokemon(carrier)
        if holder is None or is_in_active_spot(holder):
            return False
        if not (calc.is_attack and calc.is_opposing):
            return False
        if calc.target.owning_player_id != holder.owning_player_id:
            return False
        return calc.attacker is not None \
            and _attacker_energy_count(calc.attacker) <= 2


card = PokemonCardDef(
    guid="415b1d30-c648-5c86-b84e-00e20262825c",
    key="ME5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bastiodon.Name",
    display_name="Bastiodon",
    searchable_by=["Bastiodon", "Stage 2", "Bastiodon"],
    subtypes=["Stage 2"],
    collector_number=62,
    set_code="ME5",
    rarity=Rarities.Rare,
    hp=160,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Shieldon.Name",
    family_id=410,
    abilities=[
        Ability(
            title="Ancient Bulwark",
            game_text="As long as this Pok\u00e9mon is on your Bench, prevent all damage done to each of your Pok\u00e9mon by attacks from your opponent's Pok\u00e9mon that have 2 or less Energy attached.",
            passive=AncientBulwarkPassive(),
        ),
        Attack(
            title="Hammer In",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=160,
        ),
    ],
)