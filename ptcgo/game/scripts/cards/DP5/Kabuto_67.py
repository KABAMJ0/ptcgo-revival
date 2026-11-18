from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import search_to_bench
from ptcgo.game.card_effects.attacks_common import flip_or_nothing
from ptcgo.game.card_effects.trainers import any_of, named_exactly

card = PokemonCardDef(
    guid="71874857-0603-507d-8cf0-36476467d769",
    key="DP5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Kabuto.Name",
    display_name="Kabuto",
    searchable_by=["Kabuto", "Stage 1", "Kabuto"],
    subtypes=["Stage 1"],
    collector_number=67,
    set_code="DP5",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.DomeFossil.Name",
    family_id=140,
    abilities=[
        Ability(
            title="Ancient Guidance",
            game_text="Once during your turn (before your attack), you may flip a coin. If heads, search your deck for Helix Fossil, Dome Fossil, or Old Amber and put it onto your Bench. Shuffle your deck afterward. This power can't be used if Kabuto is affected by a Special Condition.",
            activation=Activations.ONCE_PER_TURN,
            effect=flip_or_nothing(then=search_to_bench(any_of(named_exactly("helix fossil"), named_exactly("dome fossil"), named_exactly("old amber")), count=1)),
        ),
        Attack(
            title="Shell Attack",
            cost={PokemonTypes.FIGHTING: 1},
            damage=20,
        ),
    ],
)