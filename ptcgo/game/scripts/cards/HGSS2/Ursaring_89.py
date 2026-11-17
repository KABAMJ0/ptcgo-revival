from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="86f39069-e198-5691-9cad-c5b2f204f820",
    key="HGSS2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ursaring.Name",
    display_name="Ursaring",
    searchable_by=["Ursaring", "Stage 1", "Prime", "Ursaring"],
    subtypes=["Stage 1", "Prime"],
    collector_number=89,
    set_code="HGSS2",
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Teddiursa.Name",
    family_id=216,
    abilities=[
        Ability(
            title="Berserk",
            game_text="If Ursaring has any damage counters on it, each of Ursaring's attacks does 60 more damage (before applying Weakness and Resistance).",
            effect=unimplemented,
        ),
        Attack(
            title="Hammer Arm",
            game_text="Discard the top card from your opponent's deck.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=30,
            effect=unimplemented,
        ),
        Attack(
            title="Megaton Lariat",
            cost={PokemonTypes.COLORLESS: 4},
            damage=60,
        ),
    ],
)