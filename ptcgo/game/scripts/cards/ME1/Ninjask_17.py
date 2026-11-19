from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Triggers
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import search_to_bench, switch_self_attack
from ptcgo.game.card_effects.trainers import named_exactly

card = PokemonCardDef(
    guid="b5392403-e978-5270-a1e8-214f02a715dc",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ninjask.Name",
    display_name="Ninjask",
    searchable_by=["Ninjask", "Stage 1", "Ninjask"],
    subtypes=["Stage 1"],
    collector_number=17,
    set_code="ME1",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Nincada.Name",
    family_id=290,
    abilities=[
        Ability(
            title="Cast-Off Shell",
            game_text="Once during your turn, when you play this Pok\u00e9mon from your hand to evolve 1 of your Pok\u00e9mon, you may use this Ability. Search your deck for a Shedinja and put it onto your Bench. Then, shuffle your deck.",
            trigger=Triggers.ON_EVOLVE,
            effect=search_to_bench(named_exactly("shedinja"), count=1),
        ),
        Attack(
            title="U-turn",
            game_text="Switch this Pok\u00e9mon with 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=90,
            effect=switch_self_attack(),
        ),
    ],
)