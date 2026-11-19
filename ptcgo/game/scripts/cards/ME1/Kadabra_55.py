from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import draw_attack

card = PokemonCardDef(
    guid="5d429cb0-be48-55c0-8965-718e53057b83",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Kadabra.Name",
    display_name="Kadabra",
    searchable_by=["Kadabra", "Stage 1", "Kadabra"],
    subtypes=["Stage 1"],
    collector_number=55,
    set_code="ME1",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Abra.Name",
    family_id=63,
    abilities=[
        Ability(
            title="Psychic Draw",
            game_text="Once during your turn, when you play this Pok\u00e9mon from your hand to evolve 1 of your Pok\u00e9mon, you may use this Ability. Draw 2 cards.",
            trigger=Triggers.ON_EVOLVE,
            effect=draw_attack(2),
        ),
        Attack(
            title="Super Psy Bolt",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=30,
        ),
    ],
)