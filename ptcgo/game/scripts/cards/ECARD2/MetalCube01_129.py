from ptcgo.game.data_utils import PokemonToolCardDef, Attack, Ability, Triggers
from ptcgo.game.attributes import Rarities, PokemonTypes
from ptcgo.game.card_effects.trainers import discard_tool_at_end_of_turn, pokemon_of, switch
from ptcgo.game.card_effects.support_common import gust_attack

card = PokemonToolCardDef(
    guid="87584bc2-9241-51ed-b3b0-368b1887fa61",
    key="ECARD2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MetalCube01.Name",
    display_name="Metal Cube 01",
    searchable_by=["Metal Cube 01", "Technical Machine"],
    subtypes=["Technical Machine"],
    collector_number=129,
    set_code="ECARD2",
    rarity=Rarities.Uncommon,
    granted_abilities=[
        Attack(
            title="Metal Reversal",
            game_text="Before doing damage, you may choose 1 of your opponent's Benched Pokémon and switch it with the Defending Pokémon.",
            cost={PokemonTypes.METAL: 1},
            damage=10,
            effect=gust_attack(damage_to_new_active=10, damage_before=0),
        ),
        Ability(
            title="Metal Cube 01",
            game_text="Discard this card at the end of your turn.",
            trigger=Triggers.END_OF_TURN,
            effect=discard_tool_at_end_of_turn(),
        ),
    ],
    attach_to=pokemon_of("metal"),
)
