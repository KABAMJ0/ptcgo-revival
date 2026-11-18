from ptcgo.game.data_utils import PokemonToolCardDef, Ability, Triggers
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import exp_share_on_ally_ko

card = PokemonToolCardDef(
    guid="c5002888-290e-5be1-a8d2-3dc121703ab4",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ExpShare.Name",
    display_name="Exp. Share",
    searchable_by=["Exp. Share", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=174,
    set_code="SV1",
    rarity=Rarities.Uncommon,
    granted_abilities=[
        Ability(
            title="Exp. Share",
            game_text="When your Active Pokémon is Knocked Out by damage from an attack from your opponent's Pokémon, you may move a Basic Energy from that Pokémon to the Pokémon this card is attached to. Attach a Pokémon Tool to 1 of your Pokémon that doesn't already have a Pokémon Tool attached.",
            trigger=Triggers.ON_ALLY_KNOCKED_OUT,
            effect=exp_share_on_ally_ko(),
        ),
    ],
)
