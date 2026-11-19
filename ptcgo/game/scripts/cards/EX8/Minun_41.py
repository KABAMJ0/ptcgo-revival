from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import recover_from_discard


card = PokemonCardDef(
    guid="d616de21-6170-50d5-8159-bffbaab4da0c",
    key="EX8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Minun.Name",
    display_name="Minun",
    searchable_by=["Minun", "Basic", "Minun"],
    subtypes=["Basic"],
    collector_number=41,
    set_code="EX8",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=312,
    abilities=[
        Attack(
            title="Sniff Out",
            game_text="Put any 1 card from your discard pile into your hand.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=recover_from_discard(count=1),
        ),
        Attack(
            title="Negative Spark",
            game_text="Does 20 damage to each of your opponent's Pok\u00e9mon that has any Pok\u00e9-Bodies. Don't apply Weakness and Resistance.",
            cost={PokemonTypes.LIGHTNING: 1},
            effect=unimplemented,
        ),
    ],
)