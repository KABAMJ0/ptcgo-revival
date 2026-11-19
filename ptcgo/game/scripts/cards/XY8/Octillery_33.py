from ptcgo.game.data_utils import Ability, Activations, Attack, PokemonCardDef, unimplemented
from ptcgo.game.card_effects.support_common import draw_until_effect
from ptcgo.game.attributes import PokemonStage, PokemonTypes, Rarities
from ptcgo.game.card_effects.attacks_common import no_retreat_attack

card = PokemonCardDef(
    guid="2aae843e-e0e7-50c3-b3be-a20f008dac41",
    key="XY8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Octillery.Name",
    display_name="Octillery",
    searchable_by=["Octillery", "Stage 1", "Octillery"],
    subtypes=["Stage 1"],
    collector_number=33,
    set_code="XY8",
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Remoraid.Name",
    family_id=223,
    abilities=[
        Ability(
            title="Abyssal Hand",
            game_text="Once during your turn (before your attack), you may draw cards until you have 5 cards in your hand.",
            effect=draw_until_effect(5),
        ),
        Attack(
            title="Hug",
            game_text="The Defending Pok\u00e9mon can't retreat during your opponent's next turn.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=40,
            effect=no_retreat_attack(),
        ),
    ],
)