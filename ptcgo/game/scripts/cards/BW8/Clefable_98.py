from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import evolve_from_deck, flip_or_nothing

card = PokemonCardDef(
    guid="a20bf86c-5341-5553-acb8-883c552eeda3",
    key="BW8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Clefable.Name",
    display_name="Clefable",
    searchable_by=["Clefable", "Stage 1", "Clefable"],
    subtypes=["Stage 1"],
    collector_number=98,
    set_code="BW8",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Clefairy.Name",
    family_id=35,
    abilities=[
        Ability(
            title="Moon Guidance",
            game_text="Once during your turn (before your attack), you may flip a coin. If heads, search your deck for a card that evolves from 1 of your Pok\u00e9mon and put it onto that Pok\u00e9mon. (This counts as evolving that Pok\u00e9mon.) Shuffle your deck afterward.",
            activation=Activations.ONCE_PER_TURN,
            effect=flip_or_nothing(then=evolve_from_deck()),
        ),
        Attack(
            title="Moon Impact",
            cost={PokemonTypes.COLORLESS: 3},
            damage=50,
        ),
    ],
)