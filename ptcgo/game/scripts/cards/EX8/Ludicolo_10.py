from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="ab24f9c6-48ef-5ba6-8d9d-5e05a7d4cf00",
    key="EX8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ludicolo.Name",
    display_name="Ludicolo",
    searchable_by=["Ludicolo", "Stage 2", "Ludicolo"],
    subtypes=["Stage 2"],
    collector_number=10,
    set_code="EX8",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Lombre.Name",
    family_id=270,
    abilities=[
        Ability(
            title="Swing Dance",
            game_text="Once during your turn (before your attack), you may draw a card. This power can't be used if Ludicolo is affected by a Special Condition.",
            effect=unimplemented,
        ),
        Attack(
            title="Healing Steps",
            game_text="You may discard as many cards as you like from your hand. If you do, remove that many damage counters from Ludicolo.",
            cost={PokemonTypes.WATER: 1},
            damage=30,
            effect=unimplemented,
        ),
        Attack(
            title="Circular Steps",
            game_text="Does 10 damage times the number of Pok\u00e9mon in play (both yours and your opponent's), excluding Ludicolo.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=10,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)