from ptcgo.game.data_utils import PokemonToolCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import pokemon_named
from ptcgo.game.session.passives import Passive, carrier_pokemon


class BrocksProtectionPassive(Passive):
    """Energy attached to the holder can't be removed by the opponent."""

    def blocks_energy_removal(self, energy, mover_player_id, carrier):
        holder = carrier_pokemon(carrier)
        if holder is None:
            return False
        return mover_player_id != holder.owning_player_id


card = PokemonToolCardDef(
    guid="9ed498bf-e15e-5592-9623-f8272c4bb34c",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BrocksProtection.Name",
    display_name="Brock's Protection",
    searchable_by=["Brock's Protection", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=101,
    set_code="GYM2",
    rarity=Rarities.Rare,
    attach_to=pokemon_named("brock"),
    passive=BrocksProtectionPassive(),
)
