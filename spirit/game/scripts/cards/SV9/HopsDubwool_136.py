from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="f3885f13-5a6b-5870-9765-7276eca370d1",
    key="SV9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HopsDubwool.Name",
    display_name="Hop's Dubwool",
    searchable_by=["Hop's Dubwool", "Stage 1", "HopsDubwool"],
    subtypes=["Stage 1"],
    collector_number=136,
    set_code="SV9",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.HopsWooloo.Name",
    family_id=831,
    abilities=[
        Ability(
            title="Defiant Horn",
            game_text="When you play this Pok\u00e9mon from your hand to evolve 1 of your Pok\u00e9mon during your turn, you may switch in 1 of your opponent's Benched Pok\u00e9mon to the Active Spot.",
            effect=unimplemented,
        ),
        Attack(
            title="Headbutt",
            cost={PokemonTypes.COLORLESS: 3},
            damage=80,
        ),
    ],
)