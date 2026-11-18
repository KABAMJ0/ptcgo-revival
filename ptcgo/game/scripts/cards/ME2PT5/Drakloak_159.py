from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

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
            effect=unimplemented,
        ),
        Attack(
            title="Dragon Headbutt",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.PSYCHIC: 1},
            damage=70,
        ),
    ],
)