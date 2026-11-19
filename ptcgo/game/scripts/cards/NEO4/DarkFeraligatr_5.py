from ptcgo.game.card_effects.passives_common import is_in_active_spot
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, subtypes_for
from ptcgo.game.attributes import AttrID, PokemonTypes, PokemonStage, Rarities
from ptcgo.game.session.passives import Passive, carrier_pokemon


class _Scare(Passive):
    """While Dark Feraligatr is a clean Active, the opponent's Baby Pokemon
    cannot attack and their Baby Powers are off."""

    def _covers(self, pokemon, carrier) -> bool:
        holder = carrier_pokemon(carrier)
        if holder is None or pokemon.owning_player_id == carrier.owning_player_id:
            return False
        if not is_in_active_spot(holder):
            return False
        if holder.get_attribute(AttrID.SPECIAL_CONDITIONS):
            return False
        return "Baby" in subtypes_for(pokemon.archetype_id)

    def blocks_attack(self, pokemon, carrier):
        return self._covers(pokemon, carrier)

    def blocks_abilities(self, pokemon, carrier):
        return self._covers(pokemon, carrier)


async def _crushing_blow(ctx):
    """Crushing Blow: heads drops one of the Defending Pokemon's Energy."""
    await ctx.deal_damage()
    defender = ctx.defender
    if defender is None or ctx.effects_blocked(defender):
        return
    if not ctx.attached_energies(defender):
        return
    heads = await ctx.flip_coins(1, "Crushing Blow")
    if heads and all(heads):
        await ctx.discard_energy_from(defender, 1)

card = PokemonCardDef(
    guid="43e8fbce-e3c5-5b6c-8d24-e54c503366a0",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DarkFeraligatr.Name",
    display_name="Dark Feraligatr",
    searchable_by=["Dark Feraligatr", "Stage 2", "DarkFeraligatr"],
    subtypes=["Stage 2"],
    collector_number=5,
    set_code="NEO4",
    rarity=Rarities.RareHolo,
    hp=80,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.DarkCroconaw.Name",
    family_id=158,
    abilities=[
        Ability(
            title="Scare",
            game_text="As long as Dark Feraligatr is your Active Pok\u00e9mon, all of your opponent's Baby Pok\u00e9mon Powers stop working and your opponent's Baby Pok\u00e9mon can't attack. This power stops working while Dark Feraligatr is Asleep, Confused, or Paralyzed.",
            passive=_Scare(),
        ),
        Attack(
            title="Crushing Blow",
            game_text="If the Defending Pok\u00e9mon has any Energy cards attached to it, flip a coin. If heads, choose 1 of those cards and discard it.",
            cost={PokemonTypes.WATER: 3},
            damage=50,
            effect=_crushing_blow,
        ),
    ],
)