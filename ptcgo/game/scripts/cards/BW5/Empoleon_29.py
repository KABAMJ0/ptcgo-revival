from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Activations
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import discard_then_draw

card = PokemonCardDef(
    guid="7fb80cb3-2500-57d9-a510-3a6895a1a8bd",
    key="BW5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Empoleon.Name",
    display_name="Empoleon",
    searchable_by=["Empoleon", "Stage 2", "Empoleon"],
    subtypes=["Stage 2"],
    collector_number=29,
    set_code="BW5",
    rarity=Rarities.RareHolo,
    hp=140,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Prinplup.Name",
    family_id=393,
    abilities=[
        Ability(
            title="Diving Draw",
            game_text="Once during your turn (before your attack), you may discard 1 card from your hand. If you do, draw 2 cards.",
            activation=Activations.ONCE_PER_TURN,
            effect=discard_then_draw(1, 2, optional=True),
        ),
        Attack(
            title="Attack Command",
            game_text="Does 10 damage times the number of Pok\u00e9mon in play (both yours and your opponent's).",
            cost={PokemonTypes.WATER: 1},
            damage=10,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)