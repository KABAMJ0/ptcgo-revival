from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import heal_attack

card = PokemonCardDef(
    guid="38ba9c4f-08d4-579e-9f4b-d32d92e86277",
    key="SV9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Alcremieex.Name",
    display_name="Alcremie ex",
    searchable_by=["Alcremie ex", "Stage 1", "ex", "Alcremieex"],
    subtypes=["Stage 1", "ex"],
    collector_number=75,
    set_code="SV9",
    rarity=Rarities.Rare,
    hp=250,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Milcery.Name",
    family_id=868,
    abilities=[
        Ability(
            title="Confectionary Gift",
            game_text="Once during your turn, you may heal 30 damage from 1 of your Pok\u00e9mon.",
            effect=heal_attack(30, target="choice"),
        ),
        Attack(
            title="Whipped Shot",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=160,
        ),
    ],
)