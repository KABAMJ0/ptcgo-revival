from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="685b62a2-5c37-552a-99bc-9ae476b7afc8",
    key="SV3PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Beedrill.Name",
    display_name="Beedrill",
    searchable_by=["Beedrill", "Stage 2", "Beedrill"],
    subtypes=["Stage 2"],
    collector_number=15,
    set_code="SV3PT5",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Kakuna.Name",
    family_id=13,
    abilities=[
        Attack(
            title="Nadir Needle",
            game_text="If you have no cards in your hand, this attack does 120 more damage, and your opponent's Active Pok\u00e9mon is now Paralyzed and Poisoned.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="+",
            effect=unimplemented,
        ),
        Attack(
            title="Pierce",
            cost={PokemonTypes.GRASS: 2},
            damage=110,
        ),
    ],
)