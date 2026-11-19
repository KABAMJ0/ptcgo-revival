from ptcgo.game.data_utils import PokemonToolCardDef, Attack, Ability, Triggers
from ptcgo.game.attributes import Rarities, PokemonTypes
from ptcgo.game.card_effects.trainers import discard_tool_at_end_of_turn, pokemon_of
from ptcgo.game.card_effects.attacks_common import flip_damage, damage_counters_on

card = PokemonToolCardDef(
    guid="8f288a6d-2d07-553c-9a8c-63c0cfabd9a4",
    key="ECARD2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FightingCube01.Name",
    display_name="Fighting Cube 01",
    searchable_by=["Fighting Cube 01", "Technical Machine"],
    subtypes=["Technical Machine"],
    collector_number=121,
    set_code="ECARD2",
    rarity=Rarities.Uncommon,
    granted_abilities=[
        Attack(
            title="Violent Rage",
            game_text="Flip a number of coins equal to the number of damage counters on this Pokémon. This attack does 10 damage times the number of heads.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=10,
            damage_operator="x",
            effect=flip_damage(per_heads=10,
                               coins_from=damage_counters_on("self")),
        ),
        Ability(
            title="Fighting Cube 01",
            game_text="Discard this card at the end of your turn.",
            trigger=Triggers.END_OF_TURN,
            effect=discard_tool_at_end_of_turn(),
        ),
    ],
    attach_to=pokemon_of("fighting"),
)
