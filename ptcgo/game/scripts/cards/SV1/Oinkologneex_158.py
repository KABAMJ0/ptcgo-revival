from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="1fb9b5d3-6865-5b06-b3b4-460a14a84f18",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Oinkologneex.Name",
    display_name="Oinkologne ex",
    searchable_by=["Oinkologne ex", "Stage 1", "ex", "Oinkologneex"],
    subtypes=["Stage 1", "ex"],
    collector_number=158,
    set_code="SV1",
    rarity=Rarities.Rare,
    hp=260,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Lechonk.Name",
    family_id=915,
    abilities=[
        Attack(
            title="Maddening Scent",
            game_text="This attack does 30 more damage for each of your opponent's Benched Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="+",
            effect=unimplemented,
        ),
        Attack(
            title="Heavy Stomp",
            game_text="Flip a coin. If tails, during your next turn, this Pok\u00e9mon can't attack.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=210,
            effect=unimplemented,
        ),
    ],
)