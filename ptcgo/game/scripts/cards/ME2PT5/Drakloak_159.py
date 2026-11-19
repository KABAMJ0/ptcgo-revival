from ptcgo.game.data_utils import Ability, Activations, Attack, PokemonCardDef
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import look_at_top

card = PokemonCardDef(
    guid="273c817a-4f25-52e3-9f57-9dbfff03917b",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Drakloak.Name",
    display_name="Drakloak",
    searchable_by=["Drakloak", "Stage 1", "Drakloak"],
    subtypes=["Stage 1"],
    collector_number=159,
    set_code="ME2PT5",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Dreepy.Name",
    family_id=885,
    abilities=[
        Ability(
            title="Recon Directive",
            game_text="Once during your turn, you may look at the top 2 cards of your deck and put 1 of them into your hand. Put the other card on the bottom of your deck.",
            activation=Activations.ONCE_PER_TURN,
            effect=look_at_top(2, take=1, rest="bottom"),
        ),
        Attack(
            title="Dragon Headbutt",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.PSYCHIC: 1},
            damage=70,
        ),
    ],
)