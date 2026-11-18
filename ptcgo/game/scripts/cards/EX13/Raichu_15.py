from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="c477385f-7aa4-511e-8010-64ce5f68c4f1",
    key="EX13",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Raichu.Name",
    display_name="Raichu δ",
    searchable_by=["Raichu \u03b4", "Stage 1", "Raichu"],
    subtypes=["Stage 1"],
    collector_number=15,
    set_code="EX13",
    rarity=Rarities.RareHolo,
    hp=70,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Pikachu.Name",
    family_id=25,
    abilities=[
        Attack(
            title="Zzzap",
            game_text="Does 20 damage to each Pok\u00e9mon that has any Pok\u00e9-Powers or Pok\u00e9-Bodies (both yours and your opponent's). Don't apply Weakness or Resistance.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Metallic Thunder",
            game_text="You may discard 2 Metal Energy attached to Raichu. If you do, this attack's base damage is 90 instead of 50.",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=50,
            effect=unimplemented,
        ),
    ],
)