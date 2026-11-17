from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="5b553a29-90a8-5e0d-95d2-d634973f7d78",
    key="PL3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Honchkrow.Name",
    display_name="Honchkrow",
    searchable_by=["Honchkrow", "Stage 1", "Honchkrow"],
    subtypes=["Stage 1"],
    collector_number=29,
    set_code="PL3",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Murkrow.Name",
    family_id=198,
    abilities=[
        Ability(
            title="Darkness Restore",
            game_text="Once during your turn (before your attack), if Honchkrow is your Active Pok\u00e9mon and your opponent's Bench isn't full, you may use this power. Search your opponent's discard pile for a Basic Pok\u00e9mon and put it onto his or her bench. This power can't be used if Honchkrow is affected by a Special Condition.",
            effect=unimplemented,
        ),
        Attack(
            title="Riot",
            game_text="Does 30 damage plus 10 more damage for each Pok\u00e9mon that isn't an evolved Pok\u00e9mon in play (both yours and your opponent's).",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)