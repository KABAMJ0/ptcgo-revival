from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.card_effects.attacks_common import spread_damage
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="976c1a05-3eeb-5d87-9bc2-3d3ee0553b67",
    key="SM6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Volcanion.Name",
    display_name="Volcanion ◇",
    searchable_by=["Volcanion \u25c7", "Basic", "Prism Star", "Volcanion"],
    subtypes=["Basic", "Prism Star"],
    collector_number=31,
    set_code="SM6",
    rarity=Rarities.Rare,
    hp=160,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=721,
    abilities=[
        Ability(
            title="Jet Geyser",
            game_text="Once during your turn (before your attack), you may discard a Water Energy card from your hand. If you do, your opponent switches their Active Pok\u00e9mon with 1 of their Benched Pok\u00e9mon.",
            effect=unimplemented,
        ),
        Attack(
            title="Sauna Blast",
            game_text="This attack does 20 damage to each of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.WATER: 3},
            damage=100,
            effect=spread_damage(20, side="opponent"),
        ),
    ],
)