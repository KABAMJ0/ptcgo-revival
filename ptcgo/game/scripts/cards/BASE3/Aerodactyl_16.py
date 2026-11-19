from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.attributes import AttrID
from ptcgo.game.card_effects.passives_common import EvolutionLockPassive
from ptcgo.game.session.passives import carrier_pokemon


class _PrehistoricPower(EvolutionLockPassive):
    """No more Evolution cards can be played by either player; off while the
    holder is Asleep, Confused or Paralyzed."""

    def blocks_evolution(self, player_id, target, carrier):
        holder = carrier_pokemon(carrier)
        if holder.get_attribute(AttrID.SPECIAL_CONDITIONS):
            return False
        return super().blocks_evolution(player_id, target, carrier)


_prehistoric_power = _PrehistoricPower(opponents_only=False)

card = PokemonCardDef(
    guid="6b2f6d72-5830-54dc-bd86-595a350f32fa",
    key="BASE3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Aerodactyl.Name",
    display_name="Aerodactyl",
    searchable_by=["Aerodactyl", "Stage 1", "Aerodactyl"],
    subtypes=["Stage 1"],
    collector_number=16,
    set_code="BASE3",
    rarity=Rarities.Rare,
    hp=60,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.MysteriousFossil.Name",
    family_id=142,
    abilities=[
        Ability(
            title="Prehistoric Power",
            game_text="No more Evolution cards can be played. This power stops working while Aerodactyl is Asleep, Confused, or Paralyzed.",
            passive=_prehistoric_power,
        ),
        Attack(
            title="Wing Attack",
            cost={PokemonTypes.COLORLESS: 3},
            damage=30,
        ),
    ],
)