from ptcgo.game.data_utils import Ability, Activations, Attack, PokemonCardDef, unimplemented
from ptcgo.game.card_effects.attacks_common import flip_or_nothing
from ptcgo.game.attributes import PokemonStage, PokemonTypes, Rarities
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Activations
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import draw_until_effect

card = PokemonCardDef(
    guid="711d51a1-08b7-5c33-8039-26b446517cfc",
    key="SWSH12PT5GG",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bibarel.Name",
    display_name="Bibarel",
    searchable_by=["Bibarel", "Stage 1", "Bibarel"],
    subtypes=["Stage 1"],
    collector_number=25,
    set_code="SWSH12PT5GG",
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Bidoof.Name",
    family_id=399,
    abilities=[
        Ability(
            title="Industrious Incisors",
            game_text="Once during your turn, you may draw cards until you have 5 cards in your hand.",
            activation=Activations.ONCE_PER_TURN,
            effect=draw_until_effect(5),
        ),
        Attack(
            title="Tail Smash",
            game_text="Flip a coin. If tails, this attack does nothing.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=100,
            effect=flip_or_nothing(),
        ),
    ],
)