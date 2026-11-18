from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="b65cc1d4-24ec-57a3-b914-840a8a8ce32c",
    key="PL1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Muk.Name",
    display_name="Muk",
    searchable_by=["Muk", "Stage 1", "Muk"],
    subtypes=["Stage 1"],
    collector_number=57,
    set_code="PL1",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Grimer.Name",
    family_id=88,
    abilities=[
        Ability(
            title="Sludge Cell",
            game_text="If Muk remains affected by any Special Conditions between turns, remove 2 damage counters from Muk.",
            effect=unimplemented,
        ),
        Attack(
            title="Strange Poison",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Poisoned. If tails, Muk is now Poisoned.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=unimplemented,
        ),
        Attack(
            title="Strange Sludge",
            game_text="If Muk is Poisoned, this attack does 50 damage plus 20 more damage and the Defending Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=50,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)