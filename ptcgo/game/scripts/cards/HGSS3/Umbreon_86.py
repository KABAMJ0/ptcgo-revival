from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="63b2f814-7a6b-5be7-8b96-870cfb41d5a1",
    key="HGSS3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Umbreon.Name",
    display_name="Umbreon",
    searchable_by=["Umbreon", "Stage 1", "Prime", "Umbreon"],
    subtypes=["Stage 1", "Prime"],
    collector_number=86,
    set_code="HGSS3",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    family_id=133,
    abilities=[
        Ability(
            title="Cloud-Covered Moon",
            game_text="Once during your turn (before your attack), if Umbreon is your Active Pok\u00e9mon, you may flip a coin. If heads, return Umbreon and all cards attached to it to your hand. This power can't be used if Umbreon is affected by a Special Condition.",
            effect=unimplemented,
        ),
        Attack(
            title="Evoblast",
            game_text="Does 50 damage plus 10 more damage for each of your Pok\u00e9mon in play that evolves from Eevee.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)