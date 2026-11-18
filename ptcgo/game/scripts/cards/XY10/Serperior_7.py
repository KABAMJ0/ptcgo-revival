from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="90bf96b4-79f2-5099-8a53-d8d4660bb411",
    key="XY10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Serperior.Name",
    display_name="Serperior",
    searchable_by=["Serperior", "Stage 2", "Serperior"],
    subtypes=["Stage 2"],
    collector_number=7,
    set_code="XY10",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Servine.Name",
    family_id=495,
    abilities=[
        Attack(
            title="Coil",
            game_text="During your next turn, this Pok\u00e9mon's attacks do 60 more damage to your opponent's Active Pok\u00e9mon (before applying Weakness and Resistance).",
            cost={PokemonTypes.COLORLESS: 1},
            damage=40,
            effect=unimplemented,
        ),
        Attack(
            title="Slashing Strike",
            game_text="This Pok\u00e9mon can't use Slashing Strike during your next turn.",
            cost={PokemonTypes.GRASS: 1},
            damage=80,
            effect=unimplemented,
        ),
    ],
)