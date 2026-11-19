from ptcgo.game.card_effects.attacks_common import damage_counters_on, damage_per
from ptcgo.game.data_utils import Ability, Attack, PokemonCardDef, unimplemented
from ptcgo.game.attributes import PokemonStage, PokemonTypes, Rarities

card = PokemonCardDef(
    guid="a0470863-39b0-5eff-98b1-3f1036178f99",
    key="SV4PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dodrio.Name",
    display_name="Dodrio",
    searchable_by=["Dodrio", "Stage 1", "Dodrio"],
    subtypes=["Stage 1"],
    collector_number=200,
    set_code="SV4PT5",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Doduo.Name",
    family_id=84,
    abilities=[
        Ability(
            title="Zooming Draw",
            game_text="Once during your turn, you may put 1 damage counter on this Pok\u00e9mon. If you do, draw a card.",
            effect=unimplemented,
        ),
        Attack(
            title="Ballistic Beak",
            game_text="This attack does 30 more damage for each damage counter on this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="+",
            effect=damage_per(damage_counters_on("self"), per=30, base=10),
        ),
    ],
)