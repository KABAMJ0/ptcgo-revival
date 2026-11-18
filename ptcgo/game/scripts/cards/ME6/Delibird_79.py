from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, Activations, unimplemented
from ptcgo.game.card_effects.trainers import is_energy_card
from ptcgo.game.card_effects.pokemon import in_active_spot
from ptcgo.game.card_effects.support_common import look_at_top
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="c3e24548-c559-5379-a0ac-bcbd9aabb89c",
    key="ME6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Delibird.Name",
    display_name="Delibird",
    searchable_by=["Delibird", "Basic", "Delibird"],
    subtypes=["Basic"],
    collector_number=79,
    set_code="ME6",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=225,
    abilities=[
        Ability(
            title="Energizing Present",
            game_text="Once during your turn, if this Pok\u00e9mon is in the Active Spot, you may use this Ability. Look at the top 6 cards of your deck, reveal an Energy card you find there, and put it into your hand. Shuffle the other cards and put them on the bottom of your deck.",
            activation=Activations.ONCE_PER_TURN,
            condition=in_active_spot,
            effect=look_at_top(6, take=1, predicate=is_energy_card, rest="bottom"),
        ),
        Attack(
            title="Beat",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)