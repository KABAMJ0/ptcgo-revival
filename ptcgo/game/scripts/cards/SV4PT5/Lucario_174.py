from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="95ad2cc9-6e1a-5d7e-bbe1-1d497d1d5607",
    key="SV4PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lucario.Name",
    display_name="Lucario",
    searchable_by=["Lucario", "Stage 1", "Lucario"],
    subtypes=["Stage 1"],
    collector_number=174,
    set_code="SV4PT5",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Riolu.Name",
    family_id=447,
    abilities=[
        Attack(
            title="Avenging Knuckle",
            game_text="If any of your Fighting Pok\u00e9mon were Knocked Out by damage from an attack during your opponent's last turn, this attack does 120 more damage.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=30,
            damage_operator="+",
            effect=unimplemented,
        ),
        Attack(
            title="Accelerating Stab",
            game_text="During your next turn, this Pok\u00e9mon can't use Accelerating Stab.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=120,
            effect=unimplemented,
        ),
    ],
)