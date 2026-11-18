from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Activations
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import place_counters

card = PokemonCardDef(
    guid="6a737033-557f-5193-8948-a756c287514b",
    key="SVault",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DecidueyeGX.Name",
    display_name="Decidueye-GX",
    searchable_by=["Decidueye-GX", "Stage 2", "GX", "DecidueyeGX"],
    subtypes=["Stage 2", "GX"],
    collector_number=47,
    set_code="SVault",
    rarity=Rarities.Rare,
    hp=240,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Dartrix.Name",
    family_id=722,
    abilities=[
        Ability(
            title="Feather Arrow",
            game_text="Once during your turn (before your attack), you may put 2 damage counters on 1 of your opponent's Pok\u00e9mon.",
            activation=Activations.ONCE_PER_TURN,
            effect=place_counters(2, target="choose_any_opponent"),
        ),
        Attack(
            title="Razor Leaf",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=90,
        ),
        Attack(
            title="Hollow Hunt-GX",
            game_text="Put 3 cards from your discard pile into your hand. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.GRASS: 1},
            effect=unimplemented,
        ),
    ],
)